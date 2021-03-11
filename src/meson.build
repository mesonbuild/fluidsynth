src_includes = include_directories(
  '.',
  'bindings',
  'drivers',
  'midi',
  'rvoice',
  'sfloader',
  'synth',
  'utils',
)

fluidsynth_sources = files(
  'bindings/fluid_cmd.c',
  'bindings/fluid_filerenderer.c',
  'bindings/fluid_ladspa.c',
  'drivers/fluid_adriver.c',
  'drivers/fluid_mdriver.c',
  'midi/fluid_midi.c',
  'midi/fluid_midi_router.c',
  'midi/fluid_seqbind.c',
  'midi/fluid_seq.c',
  'rvoice/fluid_adsr_env.c',
  'rvoice/fluid_chorus.c',
  'rvoice/fluid_iir_filter.c',
  'rvoice/fluid_lfo.c',
  'rvoice/fluid_rev.c',
  'rvoice/fluid_rvoice.c',
  'rvoice/fluid_rvoice_dsp.c',
  'rvoice/fluid_rvoice_event.c',
  'rvoice/fluid_rvoice_mixer.c',
  'sfloader/fluid_defsfont.c',
  'sfloader/fluid_samplecache.c',
  'sfloader/fluid_sffile.c',
  'sfloader/fluid_sfont.c',
  'synth/fluid_chan.c',
  'synth/fluid_event.c',
  'synth/fluid_gen.c',
  'synth/fluid_mod.c',
  'synth/fluid_synth.c',
  'synth/fluid_synth_monopoly.c',
  'synth/fluid_tuning.c',
  'synth/fluid_voice.c',
  'utils/fluid_conv.c',
  'utils/fluid_hash.c',
  'utils/fluid_list.c',
  'utils/fluid_ringbuffer.c',
  'utils/fluid_settings.c',
  'utils/fluid_sys.c',
)

# make_tables executable generates two .c files:
#
# - fluid_conv_tables.c
# - fluid_rvoice_dsp_tables.c
#
# These files are *not buildable*, but later #include'd in the real source
# files.  To assure that these two files are generated before inclusion
# (and not accidentally compiled themselves because they are .c files), we use
# additional python script, that generates those files and then additionally
# a fake header file to be used instead of dependency later on.
#
# TODO follow up with upstream to rename these two files to .inc.h or some
# other extension, so this python script won't be necessary.

make_tables_sources = files(
  'gentables/gen_conv.c',
  'gentables/gen_rvoice_dsp.c',
  'gentables/make_tables.c',
)

make_tables_exe = executable('make_tables', make_tables_sources,
                             native : true,
                             dependencies : m_dep,
                             include_directories : '.')

make_tables_py = find_program('make_tables.py')

tables = custom_target('fluid_tables',
                       command : [make_tables_py, make_tables_exe, meson.current_build_dir() + '/'],
                       output : ['fake-table-header.h'])
