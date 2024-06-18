from task1.utils import Utils
from data import Label


def test_label():
    label_dict = Utils.convert_pdf_to_dict("../task1/test_task.pdf")
    label = Label.model_validate(label_dict)
    for attribute, value in label.__dict__.items():
        print(f"{attribute}: {value}")

