Name:		texlive-luamesh
Version:	63875
Release:	2
Summary:	Computes and draws 2D Delaunay triangulation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luamesh
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamesh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luamesh.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows to compute and draw 2D Delaunay
triangulation. The algorithm is written with lua, and depending
upon the choice of the engine, the drawing is done by MetaPost
(with luamplib) or by TikZ. The Delaunay triangulation
algorithm is the Bowyer and Watson algorithm. Several macros
are provided to draw the global mesh, the set of points, or a
particular step of the algorithm.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luamesh
%{_texmfdistdir}/scripts/luamesh
%{_texmfdistdir}/metapost/luamesh
%doc %{_texmfdistdir}/doc/lualatex/luamesh

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
