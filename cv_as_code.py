from yattag import Doc
import sys

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.asis ('<!-- Global site tag (gtag.js) - Google Analytics --> \
                <script async src="https://www.googletagmanager.com/gtag/js?id=UA-101156774-11"></script> \
                <script> \
                window.dataLayer = window.dataLayer || []; \
                function gtag(){dataLayer.push(arguments);} \
                gtag(\'js\', new Date()); \
                gtag(\'config\', \'UA-101156774-11\'); \
                </script>')
        doc.stag ('link', rel='shortcut icon', href='/favicon.ico', type='image/x-icon')
        with tag('title'):
            text ('Curriculum vitae Anatolii Kalashnikov')
        with tag ('style', type="text/css"):
            doc.asis ('@font-weight: 200; font-face {font-weight: 200; font-family: Monserrat; src: url(https://fonts.googleapis.com/css2?family=Montserrat:wght@200&display=swap)}')
            doc.asis ('html {font-weight: 200; font-family: Montserrat, sans-serif;}')
            doc.asis ('#tableid {width: 100%; border-collapse: collapse; border: 2px solid white; margin-left: auto; margin-right: auto; width: 50em; }')
            doc.asis ('#main_tr {border-bottom: 4px solid #796161;}')
            doc.asis ('#h1title {text-align: center; font-weight: 200; font-size: 250%;}')
            doc.asis ('#devops_th {text-align: left; font-weight: 200; font-size: 230%; width: 50%; padding-bottom: 10px; color: red;}')
            doc.asis ('#anatoliy_th {text-align: left; font-weight: 200; font-size: 230%; width: 50%; padding-bottom: 10px; white-space: nowrap;}')
            doc.asis ('#main_tr_2 {border: 2px solid white;}')
            doc.asis ('p {font-weight: 200; font-size: 150%; text-align: left; margin: 1px}')
            doc.asis ('#skype_id {font-weight: 200; font-size: 150%; text-align: left}')
            doc.asis ('#skype_link {text-decoration: none}')
            doc.asis ('#telegram_id {font-weight: 200; font-size: 150%; text-align: left}')
            doc.asis ('#telegram_link {text-decoration: none}')
            doc.asis ('#email_id {font-weight: 200; font-size: 150%; text-align: left}')
            doc.asis ('#email_link {text-decoration: none}')
            doc.asis ('#social_id {font-weight: 200; font-size: 150%; text-align: left}')
            doc.asis ('#social_link {text-decoration: none}')
            doc.asis ('#skills {border_bottom: 4px; border-bottom: solid;}')
            doc.asis ('#skills_text {padding-top: 40px;}')
            doc.asis ('#a_href {font-weight: 200; font-size: 150%; text-align: left; padding-right: 5px;}')
            doc.asis ('a {text-decoration: none}')
            doc.asis ('#diploma { box-shadow: 0 0 10px rgba(0,0,0); margin-top: 10px;}')
            doc.asis ('#cv_as_code {text-align: right; z-index: 9999}')

    with tag('body'):
        with tag('h1', id = 'h1title'):
            text('')
        with tag ('a', id='cv_as_code', href='https://gitlab.com/anatoliykv/Python/-/blob/master/cv_as_code.py', target='_blank'):
            text ('CV as a Code')
        with tag ('div'):
            text ('Last updated')
            doc.asis ('<br>')
            text ('15.08.2020')

        with tag('table', id='tableid'):
            with tag ('tr', id='main_tr'):
                with tag ('th', id='devops_th'):
                    text ('DevOps Engineer')
                with tag ('th', id='anatoliy_th'):
                    text ('Anatolii Kalashnikov')

            with tag ('tr', id='location'):
                with tag ('th'):
                    with tag('p'):
                        text ('Location')
                with tag ('th'):
                    with tag('p'):
                        text ('Kyiv')

            with tag ('tr', id='telegram'):
                with tag ('th'):
                    with tag('p'):
                        text ('Telegram')
                with tag ('th', id='telegram_id'):
                    with tag('a', id='telegram_link', href='tg://resolve?domain=anatoliykv'):
                        text ('@anatoliykv')

            with tag ('tr', id='social'):
                with tag ('th'):
                    with tag('p'):
                        text ('Social')
                with tag ('th', id='social_id'):
                    with tag('a', id='social_link', href='https://www.linkedin.com/in/anatoliykv'):
                        text ('linkedin.com/in/anatoliykv')
                    with tag('br'):
                        with tag('a', id='social_link', href='https://gitlab.com/anatoliykv'):
                            text ('gitlab.com/anatoliykv')
            
            with tag ('tr', id='skills'):
                with tag ('th'):
                    with tag('p', id='skills_text'):
                        text ('Skills')
                with tag ('th'):
                    with tag('p'):
                        text ('')
            with tag ('tr'):
                with tag ('th'):
                    with tag('p'):
                        text ('Git')
                with tag ('th'):
                    with tag('p'):
                        text ('TCP/IP, DNS, DHCP')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/Bash-scripts'):
                        text ('Bash')
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/Python'):
                        text ('Python')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/Docker'):
                        text ('Docker Swarm')
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/kubernetes'):
                        text ('Kubernetes')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/ansible'):
                        text ('Ansible')
                with tag ('th', id='a_href'):
                    with tag('a'):
                        text ('Zabbix')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/terraform_wordpress_mysql_haproxy'):
                        text ('Terraform')
                with tag ('th', id='a_href'):
                    with tag('a'):
                        text ('Apache, Nginx, HAProxy')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/Jenkins'):
                        text ('Jenkins, GitLab-CI')
                with tag ('th', id='a_href'):
                    with tag('a'):
                        text ('Windows, Linux Servers')
            with tag ('tr'):
                with tag ('th', id='a_href'):
                    with tag('a', href='https://gitlab.com/anatoliykv/CloudFormation'):
                        text ('AWS: EC2, VPC, ELB, ASG, Cloud Formation, IAM, S3, EKS')
                with tag ('th', id='a_href'):
                    with tag('a'):
                        text ('AD, GPO, WSUS, Print Server, File server, SCCM, SCUP')
            
        
            with tag ('tr', id='skills'):
                with tag ('th'):
                    with tag('p', id='skills_text'):
                        text ('Languages')
                with tag ('th'):
                    with tag('p'):
                        text ('')
            with tag ('tr'):
                with tag ('th'):
                    with tag('p'):
                        text ('English - B1')
                        doc.asis ('<br>')
                        text ('Ukrainian, Russian - native')
                        doc.asis ('<br>')
                                     
            with tag ('tr', id='skills'):
                with tag ('th'):
                    with tag('p', id='skills_text'):
                        text ('Additional information')
                with tag ('th'):
                    with tag('p'):
                        text ('')
            with tag ('tr'):
                with tag ('th', colspan="2"):
                    with tag ('p'):
                        text ('Hard-working, friendly and responsible person, team player, quick learner.')

            with tag ('tr', id='skills'):
                with tag ('th'):
                    with tag('p', id='skills_text'):
                        text ('Certificates')
                with tag ('th'):
                    with tag('p'):
                        text ('')
            with tag ('tr'):
                with tag ('th'):
                    with tag ('a', href='https://geekbrains.ru/certificates/922213.en'):
                        doc.stag ('img', src='https://s3.eu-central-1.amazonaws.com/anatoliykv.ml/1407005_922213.en-1.jpg', id='diploma', style='height: 10%')
                    
                with tag ('th', rowspan='2'):
                    with tag ('a', href='https://s3.eu-central-1.amazonaws.com/anatoliykv.ml/DevOps+Base+ITEA-1.jpg'):
                        doc.stag('img', src='https://s3.eu-central-1.amazonaws.com/anatoliykv.ml/DevOps+Base+ITEA-1.jpg', id='diploma', style='height: 11%')
        
            with tag ('tr'):
                with tag ('th'):
                    with tag ('a', href='https://geekbrains.ru/certificates/928937.en'):
                        doc.stag ('img', src='https://s3.eu-central-1.amazonaws.com/anatoliykv.ml/1407005_928937.en-1.jpg', id='diploma', style='height: 10%')

            
                

#                    with tag ('th'):
#                    with tag('a', href='https://gitlab.com/paga.dazare/dark-riddle/-/jobs/artifacts/anatoliykv-branch/browse?job=build:ios'):
#                        doc.stag('img', src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/IOS_wordmark_%282017%29.svg/1920px-IOS_wordmark_%282017%29.svg.png', style='margin-top: 4em; margin-right: 0%; width: 80%' )

result = doc.getvalue()

with open("index.html", "w") as file_index:
    file_index.write(result)
    file_index.close()
