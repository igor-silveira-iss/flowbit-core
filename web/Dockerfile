# Build da aplicação Web (Go)
FROM golang:1.22-alpine AS build
WORKDIR /src
COPY go.mod ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -ldflags="-s -w" -o /out/flowbit-web ./cmd/web

# Imagem final mínima
FROM alpine:3.20
RUN adduser -D -u 10001 flowbit
COPY --from=build /out/flowbit-web /usr/local/bin/flowbit-web
USER flowbit
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/flowbit-web"]
