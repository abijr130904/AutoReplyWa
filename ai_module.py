from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODEL_NAME = "IzzulGod/GPT2-Indo-Instruct-Tuned"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=-1  # -1 = CPU, 0 = GPU
)

def ai_response(message: str) -> str:
    if generator is None:
        return "AI Lokal gagal dijalankan 🚨"
    
    # Prompt lebih natural untuk percakapan
    prompt = f"Percakapan:\nUser: {message}\nAI:"

    try:
        output = generator(
        prompt,
        max_new_tokens=5,    # 50 token lebih ideal untuk kalimat lengkap atau beberapa kalimat
        do_sample=True,       # Sampling acak untuk variasi jawaban
        top_k=50,             # Pilihan kata dari 50 token teratas → tetap relevan tapi tidak monoton
        top_p=0.95,           # Nucleus sampling untuk menjaga jawaban tetap masuk akal
        temperature=0.8,      # Cukup kreatif tapi tidak terlalu acak
        repetition_penalty=1.2  # Mengurangi pengulangan kata/frasa
        )

        reply = output[0]['generated_text'].replace(prompt, "").strip()
        return reply if reply else "Oke 👍"
    except Exception as e:
        return f"Error AI Lokal: {str(e)}"
