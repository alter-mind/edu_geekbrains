1. В чем плюсы нежурналируемой файловой системы?
  Скорость. Отсутствие журнала уменьшает количество обращений к жесткому диску, что положительно сказывается на быстродействии.
2. В чем плюсы журналируемой файловой системы?
  Надежность. Ошибки (упрощённое объяснение) пишутся в журнал, что избавляет от небходимости сканировать всю файловую систему в случае сбоя.
3. Что такое inode?
  Это индексный дескриптор, используется в UNIX (ext2, ext3, ext4), в нем хранится метаинформация о файлах и каталогах, по сути, вся информация о файлах.
4. Где хранится имя файла?
  Имена файлов хранятся в каталогах.
5. Можно ли увеличить кол-во inode?
  Это зависит от файловой системы. В некоторых файловых системах количество inode задается изначально, при создании файловой системы и не может быть изменено (есть исключения), в других файловых системах может быть динамечески увеличено в процессе работы файловой системы.
6. Тратится ли inode при создании жесткой ссылки?
  Нет, т.к. хардлинк это не создание файла, а создания имени для уже занятой inode.
7. Почему жесткие ссылки можно делать только в пределах одной файловой системы?
  Потому, что количество хардликов сохраняется на уровне файловой системы в метаинформации. При удалении всех хардлинков файл, по сути удаляется (по сути, файлы с нулевым количеством хардлинков перестают существовать для системы и со временем могут быть перезаписаны другими данными.)
8. Что такое . и ..?
  . является хардлинком на текущую директорию, .. на вышстоящую директорию.
9. Почему нельзя уменьшить размер файловой системы без простоя?
  Из-за необходимости проверки на фрагментацию и выполнение дефрагментации, при необходимости. Кроме того, во избежание коллизий доступа к данным со стороны других процессов.
10. Что такое суперблок в ext4?
  Суперблок - начальная точка файловой системы (блок, в котором хранятся метаданные файловой системы), содержит  информацию, необходимую для управления работой файловой системы. Наличие копий суперблока в каждой блоковой группе объясняется критической важностью этого элемента для файловой системы.
