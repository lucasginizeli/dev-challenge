import datetime
import logging
from core.models import Registro0000, RegistroC170, RegistroC100, Registro0150
from django.shortcuts import get_object_or_404


class Util:

    @staticmethod
    def datetime_format(str_date):
        format_date = '%d%m%Y'
        datetime_formated = datetime.datetime.strptime(str_date, format_date).date()
        return datetime_formated

    @staticmethod
    def solve_register(tipo, pk):
        if tipo == '0000':
            return get_object_or_404(Registro0000, pk=pk)
        elif tipo == '0150':
            return get_object_or_404(Registro0150, pk=pk)
        elif tipo == 'C100':
            return get_object_or_404(RegistroC100, pk=pk)
        elif tipo == 'C170':
            return get_object_or_404(RegistroC170, pk=pk)

    @staticmethod
    def parse_decimal(decimal):
        decimal = round(float(decimal.replace(',', '.')), 2)
        return decimal

    @staticmethod
    def save_form(form):
        try:
            if form.is_valid():
                form.save()
            else:
                logging.getLogger("error_logger").error(form.errors.as_json())
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            pass
