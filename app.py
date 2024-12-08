from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def count_vowels():
    result = None
    if request.method == "POST":
      
        input_text = request.form.get("input_text", "")
        
        vowels = "aeiouAEIOU"
        result = sum(1 for char in input_text if char in vowels)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(port=5000)