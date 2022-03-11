# Kills a process called killmenow

exec {'killer':
  command     => 'pkill -f killmeow',
  environment => '/usr/bin',
}
