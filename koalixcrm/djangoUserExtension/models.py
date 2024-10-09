# -*- coding: utf-8 -*-
from django.db import models
from koalixcrm.crm.contact.contact import Contact
from koalixcrm.crm.contact.customer_group import CustomerGroup
from koalixcrm.crm.contact.customer_billing_cycle import CustomerBillingCycle
from koalixcrm.crm.documents.contract import Contract
from koalixcrm.crm.documents.invoice import Invoice
from koalixcrm.djangoUserExtension.models import TemplateSet

# Private Equity CRM models
class Deal(models.Model):
    STAGES = [
        ('sourcing', 'Sourcing'),
        ('due_diligence', 'Due Diligence'),
        ('closing', 'Closing'),
        ('completed', 'Completed'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=50, choices=STAGES)
    investment_size = models.DecimalField(max_digits=12, decimal_places=2)
    valuation = models.DecimalField(max_digits=12, decimal_places=2)
    irr_target = models.DecimalField(max_digits=5, decimal_places=2)
    acquisition_date = models.DateField(null=True, blank=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PortfolioCompany(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    date_of_acquisition = models.DateField()
    total_investment = models.DecimalField(max_digits=12, decimal_places=2)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    ebitda = models.DecimalField(max_digits=12, decimal_places=2)
    company_overview = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Investor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    commitment = models.DecimalField(max_digits=12, decimal_places=2)
    distributions = models.DecimalField(max_digits=12, decimal_places=2)
    last_contact = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PortfolioCompanyPerformance(models.Model):
    id = models.BigAutoField(primary_key=True)
    portfolio_company = models.ForeignKey(PortfolioCompany, on_delete=models.CASCADE)
    report_date = models.DateField()
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    ebitda = models.DecimalField(max_digits=12, decimal_places=2)
    net_profit = models.DecimalField(max_digits=12, decimal_places=2)
    employee_count = models.IntegerField()

    def __str__(self):
        return f"{self.portfolio_company.name} - {self.report_date}"


# Text Paragraph in Document Template Model
class TextParagraphInDocumentTemplate(models.Model):
    template_set = models.ForeignKey(TemplateSet, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Paragraph in {self.template_set}"


# User Extension Model for Template Set and Currency
class UserExtension(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    default_template_set = models.ForeignKey('djangoUserExtension.TemplateSet', on_delete=models.CASCADE, blank=True, null=True)
    default_currency = models.ForeignKey('crm.Currency', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"User Extension for {self.user.username}"
