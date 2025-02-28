# Immagine da cui far partire
FROM alpine:3.13

# Directory in cui esegue
WORKDIR /usr/bin

# Copia l'immagine in directory specificata prima
COPY hello.sh . 

RUN chmod +x hello.sh

# Esegue nella cartella specificata
CMD ./hello.sh
