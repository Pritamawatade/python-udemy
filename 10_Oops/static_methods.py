class Chaiutilis:
    @staticmethod
    def exp(text):
        return [item.strip() for item in text.split(",")]

    
raw = "water, milk, ginger, honey"

cleaned = Chaiutilis.exp(raw)

print(cleaned)
