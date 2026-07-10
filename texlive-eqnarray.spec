%global tl_name eqnarray
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	More generalised equation arrays with numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eqnarray
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eqnarray.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines an equationarray environment, that allows more than three
columns, but otherwise behaves like LaTeX's eqnarray environment. This
environment is similar, in some ways, to the align environment of
amsmath. The package requires the array package.

