# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate log

Name:           rust-log0.4
Version:        0.4.27
Release:        %autorelease
Summary:        Lightweight logging facade for Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/log
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A lightweight logging facade for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv-devel %{_description}

This package contains library source intended for building other packages which
use the "kv" feature of the "%{crate}" crate.

%files       -n %{name}+kv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_serde-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_serde" feature of the "%{crate}" crate.

%files       -n %{name}+kv_serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_std-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_std" feature of the "%{crate}" crate.

%files       -n %{name}+kv_std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_sval-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_sval-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_sval" feature of the "%{crate}" crate.

%files       -n %{name}+kv_sval-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_unstable" feature of the "%{crate}" crate.

%files       -n %{name}+kv_unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_unstable_serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_unstable_serde-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_unstable_serde" feature of the "%{crate}" crate.

%files       -n %{name}+kv_unstable_serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_unstable_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_unstable_std-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_unstable_std" feature of the "%{crate}" crate.

%files       -n %{name}+kv_unstable_std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kv_unstable_sval-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kv_unstable_sval-devel %{_description}

This package contains library source intended for building other packages which
use the "kv_unstable_sval" feature of the "%{crate}" crate.

%files       -n %{name}+kv_unstable_sval-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_debug-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_debug" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_error-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_error" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_error-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_info-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_info" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_info-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_off-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_off" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_off-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_trace-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_trace" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_trace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+max_level_warn-devel %{_description}

This package contains library source intended for building other packages which
use the "max_level_warn" feature of the "%{crate}" crate.

%files       -n %{name}+max_level_warn-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_debug-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_debug" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_error-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_error" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_error-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_info-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_info-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_info" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_info-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_off-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_off-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_off" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_off-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_trace-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_trace" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_trace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_max_level_warn-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_max_level_warn-devel %{_description}

This package contains library source intended for building other packages which
use the "release_max_level_warn" feature of the "%{crate}" crate.

%files       -n %{name}+release_max_level_warn-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sval-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sval-devel %{_description}

This package contains library source intended for building other packages which
use the "sval" feature of the "%{crate}" crate.

%files       -n %{name}+sval-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sval_ref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sval_ref-devel %{_description}

This package contains library source intended for building other packages which
use the "sval_ref" feature of the "%{crate}" crate.

%files       -n %{name}+sval_ref-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+value-bag-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+value-bag-devel %{_description}

This package contains library source intended for building other packages which
use the "value-bag" feature of the "%{crate}" crate.

%files       -n %{name}+value-bag-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
