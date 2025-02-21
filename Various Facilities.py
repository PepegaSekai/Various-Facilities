import os
import time
import subprocess

# Variável global para armazenar o idioma
idioma_atual = 'pt'

textos = {
    'pt': {
        'titulo': 'TERMUX TOOL - Vários em 1',
        'opcoes_menu': ['Configuração Obrigatória', 'Personalização', 'Utilitários', 'Sair'],
        'obrigatorio_titulo': '[CONFIGURAÇÃO OBRIGATÓRIA] 📦',
        'perm_storage': '▼ Configurando permissões de armazenamento... 🔓',
        'atualizando': '▼ Atualizando repositórios e pacotes... 🔄',
        'ferramentas_uteis': '▼ Instalando ferramentas úteis... 🛠️',
        'config_concluida': '▼ Configuração básica concluída! ✅',
        'personalizacao_titulo': '[PERSONALIZAÇÃO] 🎨',
        'escolha_personalizacao': 'Escolha o que deseja instalar:',
        'utilidades_titulo': '[UTILIDADES] 🛠️',
        'em_breve': '🚧 EM BREVE - Atualizações futuras! 🚧',
        'saindo': 'Saindo... 👋',
        'opcao_invalida': 'Opção inválida! ❌',
        'personalizacao_opcoes': [
            'Oh My Zsh (shell melhorado) 🐚',
            'Termux Styling (cores/fontes)* 🎨',
            'Powerlevel10k (tema Zsh) ✨',
            'SSH Server (acesso remoto) 🔑',
            'Aliases úteis (atalhos) ⚡',
            'Figlet (textos estilizados) 🖋️',
            'Cowsay (vaca falante) 🐮',
            'Lolcat (cores no terminal) 🌈'
        ]
    },
    'en': {
        'titulo': 'TERMUX TOOL - All in One',
        'opcoes_menu': ['Mandatory Setup', 'Customization', 'Utilities', 'Exit'],
        'obrigatorio_titulo': '[MANDATORY SETUP] 📦',
        'perm_storage': '▼ Configuring storage permissions... 🔓',
        'atualizando': '▼ Updating repositories and packages... 🔄',
        'ferramentas_uteis': '▼ Installing useful tools... 🛠️',
        'config_concluida': '▼ Basic configuration completed! ✅',
        'personalizacao_titulo': '[CUSTOMIZATION] 🎨',
        'escolha_personalizacao': 'Choose what to install:',
        'utilidades_titulo': '[UTILITIES] 🛠️',
        'em_breve': '🚧 COMING SOON - Future updates! 🚧',
        'saindo': 'Exiting... 👋',
        'opcao_invalida': 'Invalid option! ❌',
        'personalizacao_opcoes': [
            'Oh My Zsh (improved shell) 🐚',
            'Termux Styling (colors/fonts)* 🎨',
            'Powerlevel10k (Zsh theme) ✨',
            'SSH Server (remote access) 🔑',
            'Useful aliases (shortcuts) ⚡',
            'Figlet (stylish texts) 🖋️',
            'Cowsay (talking cow) 🐮',
            'Lolcat (terminal colors) 🌈'
        ]
    },
    'es': {
        'titulo': 'TERMUX TOOL - Todo en Uno',
        'opcoes_menu': ['Configuración Obligatoria', 'Personalización', 'Utilidades', 'Salir'],
        'obrigatorio_titulo': '[CONFIGURACIÓN OBLIGATORIA] 📦',
        'perm_storage': '▼ Configurando permisos de almacenamiento... 🔓',
        'atualizando': '▼ Actualizando repositorios y paquetes... 🔄',
        'ferramentas_uteis': '▼ Instalando herramientas útiles... 🛠️',
        'config_concluida': '▼ Configuración básica completada! ✅',
        'personalizacao_titulo': '[PERSONALIZACIÓN] 🎨',
        'escolha_personalizacao': 'Elige qué instalar:',
        'utilidades_titulo': '[UTILIDADES] 🛠️',
        'em_breve': '🚧 PRÓXIMAMENTE - ¡Actualizaciones futuras! 🚧',
        'saindo': 'Saliendo... 👋',
        'opcao_invalida': '¡Opción inválida! ❌',
        'personalizacao_opcoes': [
            'Oh My Zsh (shell mejorado) 🐚',
            'Termux Styling (colores/fuentes)* 🎨',
            'Powerlevel10k (tema Zsh) ✨',
            'SSH Server (acceso remoto) 🔑',
            'Alias útiles (accesos directos) ⚡',
            'Figlet (textos estilizados) 🖋️',
            'Cowsay (vaca parlante) 🐮',
            'Lolcat (colores en terminal) 🌈'
        ]
    }
}

def limpar_tela():
    os.system('clear')

def selecionar_idioma():
    global idioma_atual
    limpar_tela()
    print("""Selecione seu idioma / Select your language / Seleccione su idioma:
    
1. 🇧🇷 Português Brasileiro
2. 🇺🇸 English
3. 🇪🇸 Español\n""")
    
    escolha = input("Digite o número / Enter number / Ingrese número: ").strip()
    idiomas = {'1': 'pt', '2': 'en', '3': 'es'}
    idioma_atual = idiomas.get(escolha, 'pt')

def secao_obrigatoria():
    limpar_tela()
    print(f"{textos[idioma_atual]['obrigatorio_titulo']}\n")
    print(f"{textos[idioma_atual]['perm_storage']}")
    os.system('termux-setup-storage')
    
    print(f"\n{textos[idioma_atual]['atualizando']}")
    os.system('pkg update -y && pkg upgrade -y')
    os.system('pkg install -y curl wget python git nano vim tree openssh')
    
    print(f"\n{textos[idioma_atual]['ferramentas_uteis']}")
    os.system('pkg install -y htop ncdu neofetch ffmpeg clang')
    os.system('pip install youtube-dl')
    
    print(f"\n{textos[idioma_atual]['config_concluida']}")
    time.sleep(2)

def secao_personalizacao():
    limpar_tela()
    print(f"{textos[idioma_atual]['personalizacao_titulo']}\n{textos[idioma_atual]['escolha_personalizacao']}\n")
    
    opcoes = [
        {'comando': 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'},
        {'comando': 'echo "Instale o aplicativo Termux:Styling da Play Store"'},
        {'comando': 'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${HOME}/.oh-my-zsh/custom/themes/powerlevel10k'},
        {'comando': 'ssh-keygen -A && echo "Inicie com: sshd"'},
        {'comando': 'echo "alias ls=\'ls --color=auto\'\nalias ll=\'ls -l\'\nalias la=\'ls -la\'" >> ${HOME}/.bashrc'},
        {'comando': 'pkg install -y figlet'},
        {'comando': 'pkg install -y cowsay'},
        {'comando': 'pkg install -y ruby && gem install lolcat'},
    ]
    
    for i, opcao in enumerate(textos[idioma_atual]['personalizacao_opcoes'], 1):
        print(f"{i}. {opcao}")
    
    escolhas = input("\n" + textos['pt']['escolha_personalizacao'] + " ").split()
    
    for escolha in escolhas:
        try:
            idx = int(escolha) - 1
            if 0 <= idx < len(opcoes):
                print(f"\n▼ Instalando: {textos[idioma_atual]['personalizacao_opcoes'][idx]}...")
                os.system(opcoes[idx]['comando'])
                time.sleep(1)
        except:
            continue
    
    print("\n✓ Concluído! / ✓ Done! / ✓ ¡Completado!")
    time.sleep(1)

def secao_utilidades():
    limpar_tela()
    print(f"{textos[idioma_atual]['utilidades_titulo']}\n\n{textos[idioma_atual]['em_breve']}")
    time.sleep(3)

def menu_principal():
    while True:
        limpar_tela()
        print(f"""╔══════════════════════════╗
║   {textos[idioma_atual]['titulo']}   ║
╠══════════════════════════╣
║ 1. {textos[idioma_atual]['opcoes_menu'][0]}  ║
║ 2. {textos[idioma_atual]['opcoes_menu'][1]}            ║
║ 3. {textos[idioma_atual]['opcoes_menu'][2]}               ║
║ 0. {textos[idioma_atual]['opcoes_menu'][3]}                      ║
╚══════════════════════════╝""")
        
        opcao = input("\n" + textos['pt']['escolha_personalizacao'] + " ")
        
        if opcao == '1':
            secao_obrigatoria()
        elif opcao == '2':
            secao_personalizacao()
        elif opcao == '3':
            secao_utilidades()
        elif opcao == '0':
            print(f"\n{textos[idioma_atual]['saindo']}")
            break
        else:
            print(f"\n{textos[idioma_atual]['opcao_invalida']}")
            time.sleep(1)

if __name__ == '__main__':
    selecionar_idioma()
    menu_principal()