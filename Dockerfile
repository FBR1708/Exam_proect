#FROM python:3.11-alpine
#RUN mkdir exam_img
#WORKDIR  exam_img
#COPY exam_1.py /exam_img
#COPY requirement.txt /exam_img
#RUN pip3 install -r requirement.txt
#ENTRYPOINT ["python", "exam_1.py"]




FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TOKEN = " "

WORKDIR /apps

COPY .. /apps



RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirement.txt

ENTRYPOINT ["python","exam_1.py"]