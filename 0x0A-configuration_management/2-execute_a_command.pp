# using the exec resourece to kill a process

exec { 'killmenow':
    command  => '/usr/bin/pkill killmenow',
    provider => 'shell',
    returns  => [0, 1],
}
