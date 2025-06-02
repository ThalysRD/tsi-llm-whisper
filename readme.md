# transcrever.py

Este projeto utiliza o modelo Whisper da OpenAI para transcrever automaticamente áudios ou vídeos em texto.

## Como funciona

O arquivo `transcrever.py` carrega o modelo de transcrição "large" do Whisper e realiza a transcrição do áudio ou vídeo especificado no caminho do arquivo. O texto transcrito é exibido no terminal.

## Pré-requisitos

- Python 3.8 ou superior
- [ffmpeg](https://ffmpeg.org/) instalado e configurado no PATH do sistema
- Instalar as dependências do Whisper:

```bash
pip install openai-whisper
```

## Como usar

1. **Edite o arquivo `transcrever.py`:**  
   Altere a variável `path` para o caminho do arquivo de áudio ou vídeo que deseja transcrever. Exemplo:

   ```python
   path = r"C:\Users\SeuUsuario\Documents\audio.mp3"
   ```

2. **Execute o script:**

   ```bash
   python transcrever.py
   ```

3. **Veja o resultado:**  
   O texto transcrito será exibido no terminal.

## Observações

- O modelo "large" é mais preciso, porém mais pesado e pode demorar para baixar na primeira execução.
- O arquivo de áudio/vídeo pode ser nos formatos suportados pelo ffmpeg (mp3, wav, mp4, m4a, etc).
- Certifique-se de que o ffmpeg está instalado e acessível pelo terminal.

## Exemplo de uso

```python
import whisper

model = whisper.load_model("large")
path = r"C:\Users\SeuUsuario\Documents\audio.mp3"
result = model.transcribe(path)
print(result['text'])
```

---
