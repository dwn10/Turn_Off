# ⚡ Power Manager

Una elegante aplicación web para gestionar el apagado o hibernación de tu sistema Windows. Esta herramienta combina la potencia de Python con una interfaz web moderna y fácil de usar, permitiendo programar operaciones de sistema de forma visual e intuitiva.

### 💫 Descripción
Power Manager transforma los comandos de sistema tradicionales en una experiencia visual moderna. Con una interfaz web responsive, temporizador en tiempo real y soporte multilingüe (Español, English, Deutsch), la aplicación hace que la gestión de energía de tu sistema sea tan simple como unos pocos clics.

### ✨ ¿Por qué Power Manager?
- **Visual**: Interfaz web moderna en lugar de comandos de consola
- **Intuitivo**: Diseño claro y controles fáciles de usar
- **Flexible**: Programa desde 1 minuto hasta 6 horas
- **Seguro**: Confirmaciones visuales y botón de cancelación
- **Multilingüe**: Disponible en tres idiomas
- **Profesional**: Ideal para entornos domésticos y empresariales

## 👨‍💻 Frontend y UI

### 🗺️ Tecnologías
- **Framework**: Streamlit 1.31.1
- **Lenguaje**: Python 3.8+
- **Navegadores**: Chrome, Firefox, Edge, Safari

### 🎨 Componentes UI
- **Barra Lateral**:
  - Selector de idioma con banderas
  - Navegación principal
- **Panel Principal**:
  - Slider de tiempo interactivo
  - Botón de inicio con estados
  - Temporizador en tiempo real
  - Indicadores de estado

### 📐 Diseño y UX
- **Estilos**:
  - CSS personalizado moderno
  - Diseño responsive
  - Animaciones suaves
  - Paleta de colores profesional
- **Experiencia**:
  - Interacción intuitiva
  - Retroalimentación visual
  - Confirmaciones claras
  - Accesibilidad mejorada

## 🌐 Alcance y Compatibilidad

### Dispositivos Soportados
- **PC de Escritorio**: Windows 10/11
- **Laptops**: Windows 10/11
- **Tablets**: Windows 10/11 (versión completa, no Windows RT)
- **Servidores**: Windows Server 2016 o superior

### Dispositivos No Soportados
- Dispositivos macOS
- Dispositivos Linux
- Dispositivos móviles (Android/iOS)
- Tablets con Windows RT
- Consolas de videojuegos

### Casos de Uso
- **Entorno Doméstico**: Programar el apagado de PC después de descargas o actualizaciones
- **Entorno Empresarial**: Gestionar el consumo energético de equipos de oficina
- **Servidores**: Programar mantenimientos o reinicios
- **Laboratorios**: Control de equipos de prueba o desarrollo

### Limitaciones
- Requiere permisos de administrador
- Solo funciona en sistemas Windows
- No soporta programación recurrente
- No guarda historial de operaciones

## 💻 Características

- ⏲️ **Temporizador Flexible**
  - Rango de 1 a 360 minutos (6 horas)
  - Visualización en tiempo real del tiempo restante
  - Cuenta regresiva con formato MM:SS

- 🌐 **Soporte Multilingüe**
  - Español (por defecto)
  - English
  - Deutsch

- 💪 **Modos de Operación**
  - Hibernación: preserva el estado actual
  - Apagado: cierre completo del sistema

- 🛡️ **Controles de Seguridad**
  - Botón de cancelación de operación
  - Confirmaciones visuales de acciones
  - Interfaz intuitiva

## 📍 Requisitos

- Python 3.8 o superior
- Windows 10/11
- Permisos de administrador para ejecutar comandos de sistema

## 💾 Instalación

1. Clona el repositorio:
```bash
git clone <url-del-repositorio>
cd power-manager
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 📂 Uso

1. Inicia la aplicación:
```bash
streamlit run app.py
```

2. En tu navegador:
   - Selecciona el tiempo deseado usando el control deslizante
   - Elige el modo (Hibernar/Apagar)
   - Haz clic en "Iniciar Temporizador"
   - Usa "Cancelar Operación" si necesitas detener el proceso

## 💬 Idiomas

La aplicación detecta automáticamente el idioma del sistema, pero puedes cambiarlo manualmente desde el menú lateral:

- 🇪🇸 Español
- 🇬🇧 English
- 🇩🇪 Deutsch

## 🛠️ Desarrollo

- Desarrollado con Streamlit 1.31.1
- Usa `subprocess` para comandos del sistema
- Implementa manejo de estado con `st.session_state`
- CSS personalizado para una mejor experiencia de usuario

## 📘 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Contribuir

Las contribuciones son bienvenidas:

1. Haz fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
