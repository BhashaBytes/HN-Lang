import subprocess

mapping = {
    "दिखाओ": "print", "dikhao": "print",
    "लेआओ": "input", "lejao": "input",
    "अगर": "if", "agar": "if",
    "वरना अगर": "elif", "warnaagar": "elif",
    "वरना": "else", "warna": "else",
    "केलिए": "for", "kelie": "for",
    "जबतक": "while", "jabtak": "while",
    "परिभाषा_करो": "def", "paribhashakaro": "def",
    "वर्ग": "class", "varg": "class",
    "लौटाओ": "return", "lautao": "return",
    "तोड़दो": "break", "toddo": "break",
    "जारी_रखो": "continue", "jaario": "continue",
    "आयात_करो": "import", "aayatkaro": "import",
    "से": "from", "se": "from",
    "के_रूप_में": "as", "saath": "as",
    "साथ": "with", "ke_saath": "with",
    "कोशिश_करो": "try", "koshishkaro": "try",
    "सिवाय": "except", "sivay": "except",
    "अंत_में": "finally", "antme": "finally",
    "सच": "True", "sach": "True",
    "झूठ": "False", "jhooth": "False",
    "कुछनहीं": "None", "kuchnahin": "None",
    "या": "or", "ya": "or",
}

def translate(code: str) -> str:
    for hin, eng in mapping.items():
        code = code.replace(hin, eng)
    return code

def run_hnlang_file(filename="test.hn"):

    with open(filename, "r", encoding="utf-8") as f:
        hindi_code = f.read()
    python_code = translate(hindi_code)
    
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)
    
    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_hnlang_file()
