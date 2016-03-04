from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class LuasocketFile(CoalFile):
    url = "https://github.com/trevex/luasocket.git"
    exports = ["include", "libs"]
    dependencies = {
        "luajit2": {
            "git": "https://github.com/trevex/coal-luajit2.git"
        }
    }
    def prepare(self):
        git_clone(self.url, 'master', 'src')
    def build(self):
        # get luajit2 include dir from generator
        lua_include_dir = self.generator.include_dirs[0] # only one dependency so first index
        default_cmake_build('src/', 'build/', '-DLUA_INCLUDE_DIR="%s"' % lua_include_dir)
    def package(self):
        # cp('build/include', 'include')
        # cp('build/*.a', 'libs/')
        # cp('build/*.lib', 'libs/')
    def info(self, generator):
        # generator.add_library("-lglad")
        # generator.add_link_dir('libs/')
        # generator.add_include_dir('include/')
        pass
