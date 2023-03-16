import streamlit as st
from streamlit_chat import message
import pandas as pd
import openai
import json

openai.api_type='azure'
openai.api_base='https://oai-bo-azwe-prod-csr.openai.azure.com/'
openai.api_key='f8ce8085901b45c4992f16b31a44071b'
openai.api_version='2022-12-01'

def gpt(prompt):
    pre_prompt = """
        Ön izlemeli hız özelliği fonksiyon kısıtlamaları aşağıdaki gibidir.
        Bu fonksiyon ör. aşağıdaki durumlarda sınırlandırılabilir ve bazen hatalı görüntülere neden olabilir:
        Trafik işaretleri nesnelerle, etiketlerle veya boya ile tamamen veya kısmen örtüldüğünde.
        Önde giden bir araca çok yaklaşıldığında.
        Geçersiz, eskimiş veya mevcut olmayan navigasyon verilerinde.
        Navigasyon sistemi dahilinde dikkate alınmayan bölgelerde.
        Navigasyondan sapma olduğunda, ör. değişen yol ayrımlarında.
        Elektronik trafik işaretlerinde.
        Yapıştırılmış trafik işareti olan otobüsleri veyakamyonları sollarken.
        Trafik işaretleri normlara uygun değilse.
        Paralel yol için geçerli olan trafik işaretlerininalgılanmasında.
        Ülkelere özgü trafik işaretlerinde veya yol ayrımlarında.
        
        BMW 925 model aracın gösterge panelindeki gösterge donanıma bağlı olarak mesafeye ilişkin bilgiler gösterge panelinde widget olarak gösterilebilir.
        Aşağıdaki bilgiler görüntülenir:
        Toplam kilometre.
        Sürüş verilerinin göstergeleri için ayarlananaralık.
        Ayarlanan aralığa bağlı olarak sıfırlanan mesafe.
        Ortalama hız.
        Gösterge panelindeki Widgetları seçin ve ayarlayın.
        
        BMW 925 model aracın gösterge panelindeki ve kontrol ekranındaki sürüş verilerinin göstergesi için aralıklar ayarlanabilir.
        1."CAR"
        2."Sürüş bilgisi"
        3."Sürüş verileri"
        4."Değerler başlangıcı"
        5.İstenilen ayarı seçin:
            "Seyahat başlangıcı": Değerler araçyakl. dört saat durduktan sonra otomatikolarak sıfırlanır.
            "Yakıt ikmali": Değerler yakıt deposunayüksek miktarda yakıt doldurulduktansonra otomatik olarak sıfırlanır.
            "Fabrika": Fabrikadan teslimden beriolan ortalama tüketim.Fabrikadan teslim tarihinden beri olan değerler gösterilir.
            "Kişisel": Son manuel sıfırlamadan beriolan değerler gösterilir. Değerler herhangibir zamanda sıfırlanabilir.
            
            
        Tüketim geçmişi:
        Tüketim geçmişinde ortalama tüketim sıfırlanan mesafeye ve sürüş moduna bağlı olarak bir diyagram şeklinde gösterilir.
    """

    response = openai.Completion.create(
        engine='oai-bo-davinci003',
        prompt=pre_prompt + prompt,
        max_tokens=1000
    )

    return response['choices'][0]['text']


placeholder = st.empty()
if prompt := st.text_input("you:"):
    message(prompt, is_user=True)
    result = gpt(prompt)
    message(result)
    prompt = None
    #placeholder = st.empty()