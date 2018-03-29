# kill a process
exec { 'execute him!':
  command  => 'pkill killmenow'
}
