# Puppet manifest to install nginx
package { 'nginx':
  ensure => installed,
}

file_line { 'redirection':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file_line { 'nginx_404_error_page':
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'error_page 404 /page_error_404.html;',
  match => '^error_page 404',
}

file_line { 'nginx_404_error_location':
  path  => '/etc/nginx/sites-enabled/default',
  line  => 'location = /page_error_404.html { root /usr/share/nginx/html; internal; }',
  after => 'error_page 404 /page_error_404.html;',
}

