# -*- coding: utf-8 -*-
# Existing KoalixCRM Imports
from koalixcrm.crm.contact.contact import *
from koalixcrm.crm.contact.customer_group import *
from koalixcrm.crm.contact.customer import *
from koalixcrm.crm.contact.postal_address import *
from koalixcrm.crm.contact.customer_billing_cycle import *
from koalixcrm.crm.contact.email_address import *
from koalixcrm.crm.contact.phone_address import *
from koalixcrm.crm.contact.supplier import *

from koalixcrm.crm.documents.contract import Contract, PostalAddressForContract
from koalixcrm.crm.documents.contract import PhoneAddressForContract, EmailAddressForContract
from koalixcrm.crm.documents.sales_document_position import Position, SalesDocumentPosition
from koalixcrm.crm.documents.sales_document import SalesDocument, PostalAddressForSalesDocument
from koalixcrm.crm.documents.sales_document import EmailAddressForSalesDocument, PhoneAddressForSalesDocument
from koalixcrm.crm.documents.sales_document import TextParagraphInSalesDocument
from koalixcrm.crm.documents.invoice import Invoice
from koalixcrm.crm.documents.purchase_confirmation import PurchaseConfirmation
from koalixcrm.crm.documents.purchase_order import PurchaseOrder
from koalixcrm.crm.documents.quote import Quote
from koalixcrm.crm.documents.payment_reminder import PaymentReminder
from koalixcrm.crm.documents.delivery_note import DeliveryNote

from koalixcrm.crm.product.currency import *
from koalixcrm.crm.product.price import *
from koalixcrm.crm.product.product import *
from koalixcrm.crm.product.product_type import *
from koalixcrm.crm.product.product_price import *
from koalixcrm.crm.product.customer_group_transform import *
from koalixcrm.crm.product.unit_transform import *
from koalixcrm.crm.product.tax import *
from koalixcrm.crm.product.unit import *

from koalixcrm.crm.reporting.agreement import *
from koalixcrm.crm.reporting.agreement_status import *
from koalixcrm.crm.reporting.agreement_type import *
from koalixcrm.crm.reporting.estimation import *
from koalixcrm.crm.reporting.estimation_status import *
from koalixcrm.crm.reporting.human_resource import *
from koalixcrm.crm.reporting.resource_manager import *
from koalixcrm.crm.reporting.resource_type import *
from koalixcrm.crm.reporting.resource_price import *
from koalixcrm.crm.reporting.generic_task_link import *
from koalixcrm.crm.reporting.task import *
from koalixcrm.crm.reporting.task_link_type import *
from koalixcrm.crm.reporting.task_status import *
from koalixcrm.crm.reporting.work import *
from koalixcrm.crm.reporting.project import *
from koalixcrm.crm.reporting.project_link_type import *
from koalixcrm.crm.reporting.project_status import *
from koalixcrm.crm.reporting.generic_project_link import *
from koalixcrm.crm.reporting.reporting_period import *
from koalixcrm.crm.reporting.reporting_period_status import *

# New models for Deal Tracking, Portfolio Management, Investor Management, and Performance Reporting

from django.db import models


# 1. Deal Tracking for Private Equity
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


# 2. Portfolio Company Management for Private Equity
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


# 3. Investor Management
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


# 4. Portfolio Company Performance Reporting
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
