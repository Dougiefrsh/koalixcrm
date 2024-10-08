from os import path
from koalixcrm import crm, djangoUserExtension
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _
from django.conf import settings
from django.core.files import File


class Command(BaseCommand):
    help = 'Install default templates given by the koalixcrm base installation.'

    @staticmethod
    def store_default_template_xsl_file(language, file_name):
        file_path = Command.path_of_default_template_file(language, file_name)
        return Command.store_xsl_file(file_path)

    @staticmethod
    def path_of_default_template_file(language, file_name):
        file_path = path.join(settings.STATIC_ROOT, "default_templates", language, file_name)
        try:
            with open(file_path, 'r'):
                pass
        except FileNotFoundError:
            print(_("File not found: ") + file_path)
            print(_("Run collectstatic command and fix potential errors"))
        return file_path

    @staticmethod
    def store_xsl_file(xsl_file_path):
        with open(xsl_file_path, 'rb') as f:
            xsl_file = djangoUserExtension.models.XSLFile()
            xsl_file.title = path.basename(xsl_file_path)
            xsl_file.xslfile.save(path.basename(xsl_file_path), File(f))
            xsl_file.save()
        return xsl_file

    def handle(self, *args, **options):
        # Create or retrieve the template set
        template_set = djangoUserExtension.models.TemplateSet.objects.create(
            title='default_template_set',
            invoiceXSLFile=Command.store_default_template_xsl_file("en", "invoice.xsl"),
            quoteXSLFile=Command.store_default_template_xsl_file("en", "quote.xsl")
        )

        if 'koalixcrm.accounting' in settings.INSTALLED_APPS:
            template_set.profitLossStatementXSLFile = Command.store_default_template_xsl_file("en", "profitlossstatement.xsl")
            template_set.balancesheetXSLFile = Command.store_default_template_xsl_file("en", "balancesheet.xsl")

        # General settings for the template set
        template_set.bankingaccountref = "xx-xxxxxx-x"
        template_set.addresser = _("John Smit, Sample Company, 8976 Smallville")
        template_set.headerTextsalesorders = _("According to your wishes the contract consists of the following positions:")
        template_set.footerTextsalesorders = _("Thank you for your interest in our company \n Best regards")
        template_set.headerTextpurchaseorders = _("We would like to order the following positions:")
        template_set.footerTextpurchaseorders = _("Best regards")
        template_set.pagefooterleft = _("Sample Company")
        template_set.pagefootermiddle = _("Sample Address")
        template_set.save()

        # Fetch or create the currency (USD)
        currency, created = crm.models.Currency.objects.get_or_create(
            short_name="USD",
            defaults={'description': 'US Dollar', 'rounding': '0.10'}
        )

        # Ensure there's a user to assign the template set and currency
        user = User.objects.first()  # Ensure that there's at least one user
        if not user:
            print("No users found. Please ensure there's a user before running this command.")
            return

        # Create the user extension
        user_extension = djangoUserExtension.models.UserExtension.objects.create(
            defaultTemplateSet=template_set,
            defaultCurrency=currency,
            user=user
        )

        # Adding default user contact information
        postaladdress = djangoUserExtension.models.UserExtensionPostalAddress.objects.create(
            purpose='H',
            name="John",
            prename="Smith",
            addressline1="Ave 1",
            zipcode=899887,
            town="Smallville",
            userExtension=user_extension
        )

        phoneaddress = djangoUserExtension.models.UserExtensionPhoneAddress.objects.create(
            phone="1293847",
            purpose='H',
            userExtension=user_extension
        )

        emailaddress = djangoUserExtension.models.UserExtensionEmailAddress.objects.create(
            email="john.smith@smallville.com",
            purpose='H',
            userExtension=user_extension
        )

        self.stdout.write(self.style.SUCCESS('Default templates and USD currency successfully installed!'))
