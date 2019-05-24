# docker build -t eb_deploy -f Dockerfile .
FROM                sungmin88/eb_docker:base
ENV                 DJANGO_SETTINGS_MODULE config.settings.production
# 전체 소스코드 복사
COPY                ./  /srv/project/
WORKDIR             /srv/project


# 프로세스를 실행할 명령
WORKDIR             /srv/project/app
RUN                 python3 manage.py collectstatic --noinput

# Nginx
RUN                 rm -rf  /etc/nginx/sites-available/* && \
                    rm -rf  /etc/nginx/sites-enabled/* && \
# 프로젝트 Nginx설정파일 복사 및 enabled로 링크 설정
                    cp -f   /srv/project/.config/app.nginx \
                            /etc/nginx/sites-available/ && \
                    ln -sf  /etc/nginx/sites-available/app.nginx \
                            /etc/nginx/sites-enabled/app.nginx

# supervisor설정파일 복사
RUN                 cp -f   /srv/project/.config/supervisor.conf \
                            /etc/supervisor/conf.d/

# 80번 포트 개방
EXPOSE              80

# Command로 supervisor실행
CMD                 supervisord -n