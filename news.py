"""Small links to EDS's existing, public AI news site."""
NEWS_URL = 'https://le-brief-ia-eds.florouss.chatgpt.site/'


def news_link(label='Lire les actus IA', css='news-link'):
    return f'<a class="{css}" href="{NEWS_URL}" target="_blank" rel="noopener noreferrer">{label} <span aria-hidden="true">↗</span><span class="news-sr"> (nouvel onglet)</span></a>'


def news_home():
    return f'''<aside class="container news-bridge" aria-labelledby="news-title"><span class="news-symbol" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 5h19v21a2 2 0 0 1-2 2H7a3 3 0 0 1-3-3V12h3Z"/><path d="M7 12v13m5-14h9m-9 5h9m-9 5h4m3 0h2"/></svg></span><div class="news-copy"><p class="news-label">Le Brief IA · par EDS</p><h2 id="news-title">Gardez un œil sur ce qui change.</h2><p>Des actualités IA sourcées, avec un regard critique.</p></div>{news_link()}</aside>'''


def news_training():
    return f'''<aside class="container news-training" aria-label="Continuer votre veille après la formation"><p><strong>Pour continuer à apprendre.</strong> Retrouvez les actualités et les nouveaux usages de l’IA dans Le Brief IA, par EDS.</p>{news_link('Découvrir Le Brief IA')}</aside>'''
