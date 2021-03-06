# Class: site
#
#
class site
{
  $login    = "Admin"
  $email    = "admin@example.com"
  $password = "password"

  exec { "apt-get update":
    command => "/usr/bin/apt-get update"
  } ->

  class { "python":
    version    => "system",
    pip        => true,
    dev        => true,
    virtualenv => false,
    gunicorn   => false
  } ->

  python::requirements { "/vagrant/requirements.txt":
    owner      => "root"
  } ->

  exec { "startmisago":
    command => "python manage.py startmisago",
    path    => "/usr/bin:/usr/sbin:/bin:/usr/local/bin",
    cwd     => "/vagrant"
  } ->

  exec { "adduser":
    command => "python manage.py adduser ${login} ${email} ${password} --admin \
               && /bin/echo 'admin_user_created' >> /etc/puppet/puppet_history",
    unless  => "/bin/grep 'admin_user_created' /etc/puppet/puppet_history",
    path    => "/usr/bin:/usr/sbin:/bin:/usr/local/bin",
    cwd     => "/vagrant"
  }
}

include site
