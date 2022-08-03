FROM python:3.10.5-slim

# Set username and home folder
RUN useradd mygreensapi
WORKDIR /home/mygreensapi

# Prepare environment and packages 
COPY requirements.txt requirements.txt
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

# Copy main files
COPY api api
COPY app.py run.sh ./
RUN chmod +x run.sh

# Set ENV variable and files ownership
ENV FLASK_APP app.py
RUN chown -R mygreensapi:mygreensapi ./
USER mygreensapi

# Set external port and run the server
EXPOSE 5000
ENTRYPOINT ["./run.sh"]