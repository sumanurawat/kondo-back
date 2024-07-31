# Set your project name here
PROJECT_NAME=kondo-back
GCP_PROJECT=kondo-21401
REGION=us-east1
IMAGE_NAME=gcr.io/$(GCP_PROJECT)/$(PROJECT_NAME)

install:
	pip install -r requirements.txt

clean:
	@echo "Cleaning all uvicorn processes..."
	-@pkill -9 -f uvicorn || true
	@echo "Cleaning Python processes related to uvicorn and resource_tracker..."
	-@ps aux | grep '[v]env/bin/uvicorn' | awk '{print $$2}' | xargs -r kill -9 || true
	-@ps aux | grep '[m]ultiprocessing.resource_tracker' | awk '{print $$2}' | xargs -r kill -9 || true
	@echo "Cleaning specific port 8000..."
	-@lsof -ti :8000 | xargs -r kill -9 || true
	@echo "Clean-up done."

run: clean
	uvicorn app.main:app --reload

test:
	flake8 app
	# Add your test commands here (e.g., pytest)

format:
	black .

deploy:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .
	@echo "Pushing Docker image to Google Container Registry..."
	docker push $(IMAGE_NAME)
	@echo "Deploying to Google Cloud Run..."
	gcloud run deploy $(PROJECT_NAME) \
		--image $(IMAGE_NAME) \
		--platform managed \
		--region $(REGION) \
		--allow-unauthenticated
	@echo "Deployment complete."

.PHONY: install run test format clean deploy