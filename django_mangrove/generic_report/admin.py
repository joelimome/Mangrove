#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from django.contrib import admin
from .models import *
import eav

admin.site.register(Report)
admin.site.register(Record)  
admin.site.register(Indicator)
admin.site.register(Parameter)
admin.site.register(ReportView)
admin.site.register(SelectedIndicator)

eav.register(Record)
