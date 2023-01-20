from dj_rest_auth.forms import AllAuthPasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from jobzill.applications.utils.EmailSender import EmailSender

if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account import app_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.forms import \
        ResetPasswordForm as DefaultPasswordResetForm
    from allauth.account.forms import default_token_generator
    from allauth.account.utils import (filter_users_by_email,
                                       user_pk_to_url_str, user_username)
    from allauth.utils import build_absolute_uri


class ModifiedPasswordResetForm(AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        print("I am inside form _______________")
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email

            path = reverse(
                'rest_password_reset_confirm'
            )
            path = path + user_pk_to_url_str(user)+"/"+str(temp_key),
            url = build_absolute_uri(request, path[0])

            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
            }

            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)

            print("The urls is", url)
            print("__________Email Send for password reset ______________", context)

            try:
                email_sender = EmailSender(from_email="pradip.meerako@gmail.com",
                                        to=[user.email], subject="Create New Password", context=context, template="new_password_email.html")
                email_sender.send_mail()
            except Exception as e:
                print("exception--------->", e, Exception.__cause__, Exception.__dict__, Exception.__dir__)
        # get_adapter(request).send_mail(
        #     'account/email/password_reset_key', email, context
        # )
        return self.cleaned_data['email']
