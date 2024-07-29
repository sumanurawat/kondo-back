# Set your project name here
PROJECT_NAME=kondo-back

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

.PHONY: install run test format clean