# Kills a process called killmenow

exec {'killer':
  command     => '/usr/bin/pkill killmenow',
}
