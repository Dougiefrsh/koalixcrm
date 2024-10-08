"""
This file contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py:: 
    GRAPPELLI_INDEX_DASHBOARD = 'koalixcrm.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import gettext_lazy as _
from grappelli.dashboard import modules, Dashboard
from koalixcrm.version import KOALIXCRM_VERSION

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for Timoneer Strategic Partners.
    """

    def init_with_context(self, context):
        # Main CRM version info
        self.children.append(modules.Group(
            _('Timoneer Strategic Partners'),
            column=1,
            collapsible=True,
            children=[                
                # Private Equity Management Section (Newly Added)
                modules.ModelList(
                    _('Private Equity Features'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.models.Deal',  # Deal Tracking
                        'koalixcrm.crm.models.PortfolioCompany',  # Portfolio Company Management
                        'koalixcrm.crm.models.Investor',  # Investor Management
                        'koalixcrm.crm.models.PortfolioCompanyPerformance',  # Portfolio Company Performance
                    ),
                ),
                # Documents and Contracts (Renamed section)
                modules.ModelList(
                    _('Documents and Contracts'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.documents.contract.Contract',
                        'koalixcrm.crm.documents.quote.Quote',
                        'koalixcrm.crm.documents.invoice.Invoice',
                        # Omitted PurchaseConfirmation and DeliveryNote
                    ),
                ),
                # Scheduler Section
                modules.ModelList(
                    _('Scheduler'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.contact.contact.CallForContact',
                        'koalixcrm.crm.contact.contact.VisitForContact',
                    ),
                ),
                # Products Section
                modules.ModelList(
                    _('Products'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=('koalixcrm.crm.product.product.Product',),
                ),
                # Contacts Section
                modules.ModelList(
                    _('Contacts'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.contact.customer.Customer',
                        'koalixcrm.crm.contact.supplier.Supplier',
                        'koalixcrm.crm.contact.person.Person',
                    ),
                ),
                # Accounting Section
                modules.ModelList(
                    _('Accounting'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=('koalixcrm.accounting.*',),
                ),
                # Projects Section
                modules.ModelList(
                    _('Projects'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.reporting.project.Project',
                        'koalixcrm.crm.reporting.reporting_period.ReportingPeriod',
                        'koalixcrm.crm.reporting.task.Task',
                        'koalixcrm.crm.reporting.agreement.Agreement',
                        'koalixcrm.crm.reporting.estimation.Estimation',
                    ),
                ),
                # Report Work and Expenses Section
                modules.LinkList(
                    _('Report Work And Expenses'),
                    column=1,
                    children=[
                        {'title': _('Time Tracking'), 'url': '/koalixcrm/crm/reporting/time_tracking/', 'external': False},
                        {'title': _('Set Timezone'), 'url': '/koalixcrm/crm/reporting/set_timezone/', 'external': False},
                    ],
                ),
            ]
        ))

        # Users, Access Rights, and Application Settings Section
        self.children.append(modules.Group(
            _('Users, Access Rights and Application Settings'),
            column=1,
            collapsible=True,
            children=[
                # Administration
                modules.ModelList(
                    _('Administration'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                # Contact Settings
                modules.ModelList(
                    _('Contact settings'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.contact.customer_billing_cycle.CustomerBillingCycle',
                        'koalixcrm.crm.contact.customer_group.CustomerGroup',
                    ),
                ),
                # Product Settings
                modules.ModelList(
                    _('Product settings'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.product.tax.Tax',
                        'koalixcrm.crm.product.unit.Unit',
                        'koalixcrm.crm.product.currency.Currency',
                    ),
                ),
                # Reporting Settings
                modules.ModelList(
                    _('Reporting settings'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.crm.reporting.agreement_status.AgreementStatus',
                        'koalixcrm.crm.reporting.agreement_type.AgreementType',
                        'koalixcrm.crm.reporting.estimation_status.EstimationStatus',
                        'koalixcrm.crm.reporting.generic_project_link.GenericProjectLink',
                        'koalixcrm.crm.reporting.generic_task_link.GenericTaskLink',
                        'koalixcrm.crm.reporting.project_link_type.ProjectLinkType',
                        'koalixcrm.crm.reporting.project_status.ProjectStatus',
                        'koalixcrm.crm.reporting.reporting_period_status.ReportingPeriodStatus',
                        'koalixcrm.crm.reporting.resource.Resource',
                        'koalixcrm.crm.reporting.resource_manager.ResourceManager',
                        'koalixcrm.crm.reporting.resource_type.ResourceType',
                        'koalixcrm.crm.reporting.task_link_type.TaskLinkType',
                        'koalixcrm.crm.reporting.task_status.TaskStatus',
                    ),
                ),
                # PDF Document Settings
                modules.ModelList(
                    _('PDF document settings'),
                    column=1,
                    css_classes=('collapse closed',),
                    models=(
                        'koalixcrm.djangoUserExtension.user_extension.document_template.*',
                        'koalixcrm.djangoUserExtension.user_extension.template_set.TemplateSet',
                        'koalixcrm.djangoUserExtension.user_extension.user_extension.*',
                    ),
                ),
            ]
        ))

        # Media Management and Support Sections
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=2,
            children=[{'title': _('FileBrowser'), 'url': '/admin/filebrowser/browse/', 'external': False}],
        ))

        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[                
                {'title': _('koalixcrm on github'), 'url': 'https://github.com/scaphilo/koalixcrm/', 'external': True},
                {'title': _('Django Documentation'), 'url': 'http://docs.djangoproject.com/', 'external': True},
                {'title': _('Grappelli Documentation'), 'url': 'http://packages.python.org/django-grappelli/', 'external': True},
            ]
        ))

        # Feed for Latest Django News
        self.children.append(modules.Feed(
            _('Latest Django News'),
            column=2,
            feed_url='http://www.djangoproject.com/rss/weblog/',
            limit=5,
        ))

        # Recent Actions
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
