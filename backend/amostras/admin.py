from django.contrib import admin
from django.utils.safestring import mark_safe
import qrcode
from io import BytesIO
import base64
from decouple import config
from .models import DadosCientificos, Amostra

@admin.register(DadosCientificos)
class DadosCientificosAdmin(admin.ModelAdmin):
    pass

@admin.register(Amostra)
class AmostraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_cientifico", "mostrar_qrcode", "mostrar_url")

    def mostrar_qrcode(self, obj):
        base_url = config("URL_TEST", default="https://127.0.0.1:8000")
        amostra_url = f"{base_url}/listagem/{obj.id}"

        qr = qrcode.make(amostra_url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        img_data = buffer.getvalue()
        img_base64 = base64.b64encode(img_data).decode()

        html = f'''
            <div style="text-align:center">
                <img src="data:image/png;base64,{img_base64}" width="100" height="100" /><br/>
                <a href="data:image/png;base64,{img_base64}" download="qrcode_amostra_{obj.id}.png"
                style="display:inline-block; margin-top:5px; padding:4px 8px; background-color:#4CAF50; color:white; border-radius:4px; text-decoration:none; font-size:12px;">
                    Baixar QR Code
                </a>
            </div>
        '''
        return mark_safe(html)


    def mostrar_url(self, obj):

        base_url = config("URL_TEST", default="https://127.0.0.1:8000")
        amostra_url = f"{base_url}/listagem/{obj.id}"

        link_html = f'<a href="{amostra_url}" target="_blank">{amostra_url}</a>'
        return mark_safe(link_html)


    mostrar_qrcode.short_description = "QR Code da Amostra"
    mostrar_url.short_description = "URL da Amostra"

admin.site.site_header = "Painel de Administração - Jardim Botânico UFSM"
admin.site.site_title = "Jardim Botânico UFSM"
admin.site.index_title = "Painel de Administração"
