# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd Turn_Off > pip install -r requirements.txt
#                          > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import subprocess
import time
import platform
import os
from datetime import datetime, timedelta

def get_system_commands():
    """Obtener comandos específicos del sistema operativo."""
    system = platform.system().lower()
    
    if system == 'windows':
        return {
            'shutdown': lambda t: f'shutdown /s /t {t}',
            'hibernate': lambda _: 'shutdown /h',
            'cancel': 'shutdown /a'
        }
    elif system == 'linux':
        # Intentar detectar el método de suspensión disponible
        suspend_command = 'pm-suspend'
        if os.path.exists('/usr/sbin/pm-suspend'):
            suspend_command = 'pm-suspend'
        elif os.path.exists('/usr/bin/systemctl'):
            suspend_command = 'systemctl suspend'
        else:
            suspend_command = 'echo mem > /sys/power/state'

        # Detectar el comando de apagado disponible
        if os.path.exists('/usr/bin/systemctl'):
            shutdown_cmd = lambda t: f'systemctl poweroff --timer={t}s'
            cancel_cmd = 'systemctl cancel --type=poweroff'
        else:
            # Usar el comando shutdown con PID file para poder cancelarlo
            pid_file = '/tmp/power_manager_shutdown.pid'
            shutdown_cmd = lambda t: f'shutdown -h +{t//60} & echo $! > {pid_file}'
            cancel_cmd = f'if [ -f {pid_file} ]; then kill $(cat {pid_file}); rm {pid_file}; fi'

        return {
            'shutdown': shutdown_cmd,
            'hibernate': lambda _: suspend_command,
            'cancel': cancel_cmd
        }
    elif system == 'darwin':  # macOS
        return {
            'shutdown': lambda t: f'shutdown -h +{t//60}',
            'hibernate': lambda _: 'pmset sleepnow',
            'cancel': 'killall shutdown'
        }
    else:
        st.error(f'Sistema operativo no soportado: {system}')
        return None

def execute_command(cmd):
    """Ejecutar comando con manejo de errores."""
    try:
        subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        st.error(f'Error al ejecutar el comando: {e.stderr}')
        return False
    except OSError as e:
        st.error(f'Error del sistema: {str(e)}')
        return False

# Diccionario de traducciones
TRANSLATIONS = {
    'Español': {
        'title': 'Power Manager',
        'description': 'Gestiona el apagado o hibernación de tu sistema de forma elegante',
        'error_system_not_supported': 'Sistema operativo no soportado. Por favor, verifica la compatibilidad.',
        'timer_label': 'Temporizador',
        'select_time': 'Selecciona el tiempo en minutos',
        'mode_label': 'Modo',
        'select_action': 'Selecciona la acción a realizar',
        'hibernate': 'Hibernar',
        'shutdown': 'Apagar',
        'start_timer': '🕐 Iniciar',
        'cancel_operation': '❌ Cancelar',
        'time_help': 'Arrastra para ajustar el tiempo | 360 min = 6 H',
        'action_help': 'Elige qué hará el sistema cuando termine el tiempo',
        'system_scheduled': 'Sistema programado para {} en {} minutos',
        'operation_cancelled': '✅ Operación cancelada exitosamente',
        'preparing': 'Preparando {}',
        'developed_with': '''Developed by <a href="https://ecuador-it.com" target="_blank" style="color: #1f77b4; text-decoration: none; font-weight: bold;">ECUADOR-IT</a> | ⚙️ Power Manager v1.0''',
        'language': 'Idioma',
        'compatible_devices': '📱 Dispositivos Compatibles',
        'devices_description': '''<div class="device-list">
            <p><strong>Esta aplicación es compatible con:</strong></p>
            <ul>
                <li>💻 Computadoras de escritorio (Windows)</li>
                <li>💻 Laptops y notebooks</li>
                <li>💻 Tablets con Windows</li>
                <li>💻 Servidores Windows</li>
            </ul>
            <p class="note"><em>⚠️ Nota: No compatible con móviles Android/iOS</em></p>
        </div>'''
    },
    'English': {
        'title': 'Power Manager',
        'description': 'Manage your system shutdown or hibernation elegantly',
        'error_system_not_supported': 'Operating system not supported. Please check compatibility.',
        'timer_label': 'Timer',
        'select_time': 'Select time in minutes',
        'mode_label': 'Mode',
        'select_action': 'Select action to perform',
        'hibernate': 'Hibernate',
        'shutdown': 'Shutdown',
        'start_timer': '🕐 Start Timer',
        'cancel_operation': '❌ Cancel',
        'time_help': 'Drag to adjust time | 360 min = 6 H',
        'action_help': 'Choose what the system will do when time runs out',
        'system_scheduled': 'System scheduled to {} in {} minutes',
        'operation_cancelled': '✅ Operation successfully cancelled',
        'preparing': 'Preparing {}',
        'developed_with': '''Developed by <a href="https://ecuador-it.com" target="_blank" style="color: #1f77b4; text-decoration: none; font-weight: bold;">ECUADOR-IT</a> | ⚙️ Power Manager v1.0''',
        'language': 'Language',
        'compatible_devices': '📱 Compatible Devices',
        'devices_description': '''<div class="device-list">
            <p><strong>This application is compatible with:</strong></p>
            <ul>
                <li>💻 Desktop computers (Windows)</li>
                <li>💻 Laptops and notebooks</li>
                <li>💻 Windows tablets</li>
                <li>💻 Windows servers</li>
            </ul>
            <p class="note"><em>⚠️ Note: Not compatible with Android/iOS mobile devices</em></p>
        </div>'''
    },
    'Deutsch': {
        'title': 'Power Manager',
        'description': 'Verwalten Sie das Herunterfahren oder den Ruhezustand Ihres Systems elegant',
        'error_system_not_supported': 'Betriebssystem nicht unterstützt. Bitte überprüfen Sie die Kompatibilität.',
        'timer_label': 'Timer',
        'select_time': 'Zeit in Minuten auswählen',
        'mode_label': 'Modus',
        'select_action': 'Aktion auswählen',
        'hibernate': 'Ruhezustand',
        'shutdown': 'Herunterfahren',
        'start_timer': '🕐 Timer starten',
        'cancel_operation': '❌ Abbrechen',
        'time_help': 'Zum Anpassen der Zeit ziehen | 360 min = 6 H',
        'action_help': 'Wählen Sie, was das System nach Ablauf der Zeit tun soll',
        'system_scheduled': 'System wird in {} Minuten {}',
        'operation_cancelled': '✅ Vorgang erfolgreich abgebrochen',
        'preparing': 'Vorbereitung {}',
        'developed_with': '''Developed by <a href="https://ecuador-it.com" target="_blank" style="color: #1f77b4; text-decoration: none; font-weight: bold;">ECUADOR-IT</a> | ⚙️ Power Manager v1.0''',
        'language': 'Sprache',
        'compatible_devices': '📱 Kompatible Geräte',
        'devices_description': '''<div class="device-list">
            <p><strong>Diese Anwendung ist kompatibel mit:</strong></p>
            <ul>
                <li>💻 Desktop-Computer (Windows)</li>
                <li>💻 Laptops und Notebooks</li>
                <li>💻 Windows-Tablets</li>
                <li>💻 Windows-Server</li>
            </ul>
            <p class="note"><em>⚠️ Hinweis: Nicht kompatibel mit Android/iOS-Mobilgeräten</em></p>
        </div>'''
    }
}

# Configuración de la página
st.set_page_config(
    page_title='Power Manager',
    page_icon='⚡',
    initial_sidebar_state='expanded'
)

# Configuración de idiomas
LANGUAGES = {
    'Español': 'ES 🇪🇸',
    'English': 'EN 🇬🇧',
    'Deutsch': 'DE 🇩🇪'
}

# Selector de idioma en la barra lateral
if 'language' not in st.session_state:
    st.session_state.language = 'Español'

with st.sidebar:
    st.markdown("""
        <style>
        section[data-testid="stSidebar"] div.row-widget.stRadio > div {
            flex-direction: column;
            gap: 0.5rem;
        }
        section[data-testid="stSidebar"] div.row-widget.stRadio > div label {
            padding: 0.5rem 1rem;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 0.5rem;
            cursor: pointer;
            margin: 0;
            display: flex;
            align-items: center;
        }
        section[data-testid="stSidebar"] div.row-widget.stRadio > div label:hover {
            background: #f8f9fa;
            transform: translateY(-1px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🌐 Idioma / Language / Sprache")
    selected_language = st.radio(
        "",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=list(LANGUAGES.keys()).index(st.session_state.language),
        key="language_selector"
    )
    
    if selected_language != st.session_state.language:
        st.session_state.language = selected_language
        st.rerun()

# Obtener traducciones para el idioma seleccionado
t = TRANSLATIONS[st.session_state.language]

# Estilos CSS personalizados
st.markdown('''
    <style>
        /* Estilos generales */
        .main > div {
            padding: 2rem;
        }
        
        /* Estilos de la barra lateral */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa;
            padding: 1rem;
        }
        
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
        }
        
        section[data-testid="stSidebar"] hr {
            margin: 2rem 0;
            border-color: #dee2e6;
        }
        
        section[data-testid="stSidebar"] h3 {
            color: #1f77b4;
            font-size: 1.2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #1f77b4;
        }
        
        /* Estilos para la lista de dispositivos */
        .device-list {
            background-color: white;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-top: 0.5rem;
        }
        
        .device-list ul {
            list-style-type: none;
            padding-left: 0;
            margin: 0.5rem 0;
        }
        
        .device-list li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #f0f0f0;
            list-style-type: none;
        }
        
        .device-list li:last-child {
            border-bottom: none;
        }
        
        .device-list p {
            margin: 0.5rem 0;
        }
        
        .device-list .note {
            margin-top: 1rem;
            color: #dc3545;
            font-size: 0.9rem;
        }
        
        .device-list ul {
            margin: 1rem 0;
            padding-left: 0.5rem;
        }
        
        /* Estilos de botones */
        .stButton button {
            width: 100%;
            border-radius: 10px;
            padding: 0.75rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        div[data-testid="stButton"] button[kind="primary"] {
            background-color: #28a745 !important;
            border-color: #28a745 !important;
            color: white !important;
        }
        
        div[data-testid="stButton"] button[kind="primary"]:hover {
            background-color: #218838 !important;
            border-color: #1e7e34 !important;
            transform: translateY(-2px);
        }
        
        /* Estilos del contenedor principal */
        div[data-testid="stVerticalBlock"] > div:has(div.element-container) {
            background-color: #f8f9fa;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }
        
        /* Estilos del temporizador */
        .timer {
            font-size: 3rem !important;
            font-weight: bold !important;
            text-align: center !important;
            color: #1f77b4 !important;
            font-family: 'Courier New', monospace !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
    </style>
''', unsafe_allow_html=True)

# Título y descripción
st.subheader(f'⚡ {t["title"]}') 

# Agregar sección de dispositivos compatibles en la barra lateral
with st.sidebar:
    st.markdown("---")
    st.markdown(f"### {t['compatible_devices']}")
    st.markdown(f'''
    <div class="device-list">
        {t['devices_description']}
    </div>
    ''', unsafe_allow_html=True)

# Descripción
st.write(f'##### {t["description"]}')

# Contenedor del contador (inicialmente vacío)
contador_container = st.container()

# Contenedor principal
with st.container():
    # Primera fila: Controles principales
    col1, col2, col3 = st.columns([2,2,1])
    
    with col1:
        st.markdown(f'#### ⏲️ {t["timer_label"]}')
        tiempo = st.slider(t["select_time"], 
                          min_value=1, 
                          max_value=360, 
                          value=30,
                          help=t["time_help"])

    with col2:
        st.markdown(f'#### 💻 {t["mode_label"]}')
        accion = st.radio(
            t["select_action"],
            options=[t["hibernate"], t["shutdown"]],
            horizontal=True,
            help=t["action_help"]
        )

if 'tiempo_final' not in st.session_state:
    st.session_state.tiempo_final = None
    st.session_state.contador_activo = False

def actualizar_contador():
    if st.session_state.tiempo_final:
        tiempo_restante = st.session_state.tiempo_final - datetime.now()
        if tiempo_restante.total_seconds() > 0:
            mins = int(tiempo_restante.total_seconds() // 60)
            secs = int(tiempo_restante.total_seconds() % 60)
            return f'{mins:02d}:{secs:02d}'
        else:
            st.session_state.contador_activo = False
            return '00:00'
    return '--:--'

# Segunda fila: Botones de acción
col1, col2 = st.columns([2,1])

with col1:
    # Contenedor para los botones
    botones_col1, botones_col2 = st.columns(2)
    
    with botones_col1:
        start = st.button(t["start_timer"], type='primary')
        if start:
            segundos = tiempo * 60
            system_commands = get_system_commands()
            if not system_commands:
                st.error(t["error_system_not_supported"])
            elif accion == t["shutdown"]:
                if execute_command(system_commands['shutdown'](segundos)):
                    mensaje = t["shutdown"].lower()
                    icono = '📴'
                    st.session_state.tiempo_final = datetime.now() + timedelta(minutes=tiempo)
                    st.session_state.contador_activo = True
                    st.success(f'{icono} {t["system_scheduled"].format(mensaje, tiempo)}')
            else:
                st.session_state.hibernar = True
                st.session_state.tiempo_hibernar = segundos
                mensaje = t["hibernate"].lower()
                icono = '💤'
            
            st.session_state.tiempo_final = datetime.now() + timedelta(minutes=tiempo)
            st.session_state.contador_activo = True
            st.success(f'{icono} {t["system_scheduled"].format(mensaje, tiempo)}')

    with botones_col2:
        if st.button(t["cancel_operation"], type='secondary'):
            system_commands = get_system_commands()
            if system_commands and execute_command(system_commands['cancel']):
                st.session_state.contador_activo = False
                st.session_state.tiempo_final = None
                st.session_state.hibernar = False
                st.info(t["operation_cancelled"])

# Inicialización del estado
if 'hibernar' not in st.session_state:
    st.session_state.hibernar = False
    st.session_state.tiempo_hibernar = 0

# Actualizar el contador
if st.session_state.contador_activo:
    tiempo_actual = actualizar_contador()
    
    # Estado actual
    estado = t["hibernate"] if st.session_state.hibernar else t["shutdown"]
    icono = '💤' if st.session_state.hibernar else '📴'
    
    # Actualizar el contador en el contenedor superior
    with contador_container:
        st.markdown(f'''
            <div style="text-align: center; background: linear-gradient(135deg, #f5f7fa 0%, #e4e7eb 100%); padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin: 1rem 0;">
                <div style="display: flex; justify-content: center; align-items: center; gap: 1rem;">
                    <span style="font-size: 2.5rem;">{icono}</span>
                    <div class="timer" style="font-size: 4rem !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin: 0;">{tiempo_actual}</div>
                </div>
                <div style="margin-top: 0.5rem; font-size: 1.1rem; color: #666;">
                    {t["preparing"].format(estado.lower())}
                </div>
            </div>
        ''', unsafe_allow_html=True)
    
    # Verificar si es tiempo de hibernar
    if st.session_state.hibernar and tiempo_actual == '00:00':
        system_commands = get_system_commands()
        if system_commands and execute_command(system_commands['hibernate'](0)):
            st.session_state.hibernar = False
    
    time.sleep(1)
    st.rerun()

# Pie de página
st.markdown('---')
st.markdown(f'''
    <div style="text-align: center; color: #666; padding: 1rem;">
        💻 {t["developed_with"]}
    </div>
''', unsafe_allow_html=True)
