#!/usr/bin/env python
version='1.0'
top = '.'
out = 'buildstuff'

def options(opt):
    opt.load('compiler_c compiler_cxx unittest_gtest')

def configure(conf):
    conf.load('compiler_c compiler_cxx unittest_gtest')

def build(ctx):

    print('id is %d' % id(ctx))

    ctx(features='cxx cxxstlib',
        source='awesome.cpp',
        target='libawesome')
         
    ctx(features='cxx cxxprogram gtest', 
        source='tests.cpp', 
        target='tests',
        use = 'libawesome')
