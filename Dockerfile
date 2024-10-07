FROM python:3.12-alpine
RUN apk add --no-cache build-base
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . ./
ENTRYPOINT ["/usr/local/bin/python3", "-m", "deflemask_preset_viewer"]
