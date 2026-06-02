# Instalación de Claude Code — IEEC

Sigue estos pasos **antes** de la Sesión 1. Si algo falla, no te preocupes:
dedicaremos los primeros minutos del taller a resolver instalaciones.

Tiempo estimado: 10–15 minutos.

---

## Requisitos previos

- Una computadora con **macOS**, **Linux** o **Windows con WSL**.
- Conexión a internet.
- Una cuenta de Anthropic (correo + contraseña). Si no la tienes, créala en
  <https://claude.ai> antes del taller.
- Saber abrir la **Terminal**:
  - **macOS**: Aplicaciones → Utilidades → Terminal.
  - **Windows**: instala WSL primero (abre PowerShell como administrador y
    ejecuta `wsl --install`, luego reinicia y abre "Ubuntu").
  - **Linux**: tu terminal de siempre.

---

## Paso 1 — Instalar Claude Code

Copia y pega esta línea en la Terminal y presiona Enter:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

El instalador descarga Claude Code y te dirá cuándo terminó. Es posible que te
pida cerrar y volver a abrir la Terminal para que el comando quede disponible.

---

## Paso 2 — Iniciar sesión

En la Terminal, ejecuta:

```bash
claude login
```

Se abrirá tu navegador para que inicies sesión con tu cuenta de Anthropic.
Autoriza el acceso y regresa a la Terminal.

---

## Paso 3 — Verificar la instalación

Ejecuta:

```bash
claude --version
```

Debe imprimir un número de versión (por ejemplo `2.x.x`). Si lo ves, la
instalación funcionó.

Ahora una prueba real. Crea una carpeta de prueba y abre Claude Code:

```bash
mkdir -p ~/prueba-claude
claude
```

Cuando aparezca el cursor, escribe:

```
hola, ¿puedes confirmar que estás funcionando?
```

Si te responde, ¡listo! Sal con `/exit` o presionando `Ctrl-C` dos veces.

---

## Paso 4 — Clonar el repositorio del taller

Tu líder de equipo te dará la dirección del repositorio. Una vez que la tengas:

```bash
git clone <DIRECCION-DEL-REPOSITORIO> taller-ia-ieec
cd taller-ia-ieec
claude
```

Con eso ya estás dentro del repositorio del taller y Claude Code puede leer las
plantillas y los datos de práctica.

---

## Solución de problemas

| Síntoma | Qué hacer |
|---------|-----------|
| `command not found: claude` | Cierra y vuelve a abrir la Terminal. Si persiste, revisa que el Paso 1 haya terminado sin error. |
| `command not found: curl` | En Linux/WSL: `sudo apt update && sudo apt install curl`. En macOS ya viene incluido. |
| `command not found: git` | macOS: ejecuta `xcode-select --install`. Linux/WSL: `sudo apt install git`. |
| El navegador no abre en el login | Copia el enlace que muestra la Terminal y pégalo manualmente en tu navegador. |
| Windows sin WSL | Abre PowerShell como administrador, ejecuta `wsl --install`, reinicia, y repite desde el Paso 1 dentro de Ubuntu. |

Si después de esto sigue sin funcionar, **toma una captura de pantalla del error**
y tráela al taller. Lo resolvemos juntos.
