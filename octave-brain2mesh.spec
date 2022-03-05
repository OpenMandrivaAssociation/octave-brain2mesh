%define octpkg brain2mesh

Summary:	A one-liner for 3D brain mesh generation for Octave
Name:		octave-%{octpkg}
Version:	0.7.9
Release:	1
Source0:	https://github.com/fangq/brain2mesh/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://mcx.space/brain2mesh

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
The Brain2Mesh toolbox provides a streamlined matlab function to convert a
segmented brain volumes and surfaces into a high-quality multi-layered
tetrahedral brain/full head mesh.

This tool does not handle the segmentation of MRI scans, but examples of
how commonly encountered segmented datasets can be used to create meshes
are available under the examples folder.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# fix file paths
mkdir inst
mkdir src
mv *.m inst
mv LICENSE.txt COPYING
cat >DESCRIPTION <<EOF
Name: %{octpkg}
Version: %{version}
Date: 2020-06-24
Author: Qianqian Fang <q.fang at neu.edu>, Anh Phong Tran <tran.anh at husky.neu.edu>
Maintainer: Qianqian Fang <q.fang at neu.edu>
Title: Brain2Mesh
Description: %{summary}.
Depends: octave (>= 4.0.0)
Autoload: no
License: GPLv3+
Categories: 3D brain mesh generation
EOF

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

