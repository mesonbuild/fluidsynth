project('fluidsynth', 'c',
        version : '2.1.7',
        license : 'LGPL-2.1-or-later',
        default_options : ['b_ndebug=if-release'],
        meson_version : '>= 0.53.0')

cc = meson.get_compiler('c')

summary('Build type', get_option('buildtype'), section : 'Build Summary')

# config file
#
# TODO there are many, many more options to set/detect in upstream template
#      see meson_options.txt for list

conf = configuration_data()

if host_machine.system() == 'darwin'
  conf.set('DARWIN', 1)
endif

conf.set('DEFAULT_SOUNDFONT', '/usr/share/soundfonts/default.sf2')

conf.set('TEST_SOUNDFONT', meson.current_source_dir() + '/sf2/VintageDreamsWaves-v2.sf2')

conf.set10('STDC_HEADERS', true)

if get_option('enable-floats')
  conf.set('WITH_FLOAT', 1)
endif
summary('Samples type',
        conf.has('WITH_FLOAT').to_string('float', 'double'),
        section : 'Developer nerds info')

headers_to_check = [
  'arpa/inet.h',        'errno.h',            'fcntl.h',
  'getopt.h',           'inttypes.h',         'io.h',
  'limits.h',           'linux/soundcard.h',  'machine/soundcard.h',
  'math.h',             'netinet/in.h',       'netinet/tcp.h',
  'pthread.h',          'signal.h',           'stdarg.h',
  'stdint.h',           'stdio.h',            'stdlib.h',
  'string.h',           'strings.h',          'sys/mman.h',
  'sys/socket.h',       'sys/soundcard.h',    'sys/stat.h',
  'sys/time.h',         'sys/types.h',        'unistd.h',
  'windows.h',
]

foreach h : headers_to_check 
  conf.set10('HAVE_' + h.underscorify().to_upper(), cc.has_header(h))
endforeach

if cc.has_function('inet_ntop', prefix : '#include <arpa/inet.h>')
  conf.set('HAVE_INETNTOP', 1) # lib uses ifdef for this one
endif

foreach fun : ['sinf', 'cosf', 'fabsf', 'powf', 'sqrtf', 'logf']
  conf.set10('HAVE_' + fun.to_upper(), cc.has_function(fun))
endforeach


# external dependencies

m_dep       = cc.find_library('m', required : false)
glib_dep    = dependency('glib-2.0', static : true)
gthread_dep = dependency('gthread-2.0', static : true)
openmp_dep  = dependency('openmp', required : false, language : 'c',
                         version : '>= 4.0')

if openmp_dep.found()
  conf.set('HAVE_OPENMP', 1)
endif
summary('OpenMP 4.0',
        openmp_dep.found().to_string('yes', 'no'),
        section : 'Developer nerds info')


# config.h

configure_file(input : 'src/config.cmake',
               output : 'config.h',
               format : 'cmake@',
               configuration : conf)


# fluidsynth lib

subdir('include')
subdir('include/fluidsynth')
subdir('src')

lib_includes = [include_directories('.', 'include'), src_includes]
dep_includes = include_directories('include')

fluidsynth_lib = library('fluidsynth', fluidsynth_sources, tables,
                         dependencies : [m_dep, glib_dep, gthread_dep, openmp_dep],
                         include_directories : lib_includes)

fluidsynth_dep = declare_dependency(link_with : fluidsynth_lib,
                                    include_directories : dep_includes)

# unit tests

subdir('test')
