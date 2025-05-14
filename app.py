
from flask import Flask, render_template, request, send_from_directory
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
IMG_FOLDER = "static/output"
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def mse(imageA, imageB):
    if imageA.shape != imageB.shape:
        imageB = cv2.resize(imageB, (imageA.shape[1], imageA.shape[0]))
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def detectar_numero_por_imagem(imagem_cv2):
    ref_dir = os.path.join(app.root_path, IMG_FOLDER)
    files = sorted([f for f in os.listdir(ref_dir) if f.endswith(".png")])

    
    imagem_cinza = cv2.resize(imagem_cv2, (100, 200))
    _, imagem_bin = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
    query = imagem_bin
    

    melhor_score = float("inf")
    melhor_numero = None

    for fname in files:
        ref_img = cv2.imread(os.path.join(ref_dir, fname), cv2.IMREAD_GRAYSCALE)
        ref_img = cv2.resize(ref_img, (100, 200))
        score = mse(query, ref_img)
        if score < melhor_score:
            melhor_score = score
            melhor_numero = int(fname.split(".")[0])

    return melhor_numero

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    imagem = None
    partes = {}

    if request.method == "POST":
       
        if "numero" in request.form and request.form["numero"].strip():
            try:
                numero = int(request.form["numero"])
                if 0 <= numero <= 9999:
                    imagem = f"{numero}.png"
                    partes = {
                        "milhar": numero // 1000,
                        "centena": (numero % 1000) // 100,
                        "dezena": (numero % 100) // 10,
                        "unidade": numero % 10
                    }
                    resultado = numero
                    return render_template("index.html", imagem=imagem, resultado=resultado, partes=partes)
            except:
                pass

        
        if "arquivo" in request.files:
            arquivo = request.files["arquivo"]
            if arquivo.filename:
                caminho_arquivo = os.path.join(UPLOAD_FOLDER, secure_filename(arquivo.filename))
                arquivo.save(caminho_arquivo)

                imagem_cv2 = cv2.imread(caminho_arquivo, cv2.IMREAD_GRAYSCALE)
                numero_detectado = detectar_numero_por_imagem(imagem_cv2)

                if numero_detectado is not None:
                    resultado = numero_detectado
                    imagem = f"{numero_detectado}.png"
                    partes = {
                        "milhar": numero_detectado // 1000,
                        "centena": (numero_detectado % 1000) // 100,
                        "dezena": (numero_detectado % 100) // 10,
                        "unidade": numero_detectado % 10
                    }

    return render_template("index.html", imagem=imagem, resultado=resultado, partes=partes)

if __name__ == "__main__":
    app.run(debug=True)
