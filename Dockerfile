FROM public.ecr.aws/lambda/python:3.8
#FROM python:3.8-slim


WORKDIR /code

#COPY ./lambda_function.py ./
COPY lambda_function.py ${LAMBDA_TASK_ROOT}
COPY ./poetry.lock /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml


ENV PATH /home/$(python3 -m site --user-base)/.local/bin:${PATH}
#ENV PATH="${PATH}:/root/.poetry/bin"
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./doc_classifier /code/doc_classifier

#CMD ["uvicorn", "doc_classifier.main:app", "--host", "0.0.0.0", "--port", "8000"]

#ENTRYPOINT ["/lambda-entrypoint.sh", "/lambda_function.lambda_handler"] 
CMD [ "lambda_function.lambda_handler" ]