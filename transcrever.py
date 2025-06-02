#importa a biblioteca whisper para transcrição de áudio
import whisper
#escolhe o modelo de transcrição large
model = whisper.load_model("large")
path = r"" #Caminho do arquivo que será transcrito
# Substitua pelo caminho do arquivo de áudio que você deseja transcrever

#transcreve o áudio do arquivo especificado
result = model.transcribe(path)
#exibe o resultado da transcrição
print(result['text'])