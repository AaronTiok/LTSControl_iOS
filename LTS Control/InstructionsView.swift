import SwiftUI

struct InstructionsView: View {
    @Environment(AccessorySessionManager.self) private var accessorySessionManager
    @Environment(LayoutModel.self) private var layoutModel
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ZStack {
                Color(uiColor: .systemBackground)
                    .ignoresSafeArea()
                ScrollView {
                    VStack(alignment: .leading, spacing: 0) {
                        
                        InstructionsRow(
                            icon: "antenna.radiowaves.left.and.right",
                            title: "建立连接",
                            description: "请确保倒料器主板已开启并安装了最新固件。"
                        )
                        Button(action: {
                            accessorySessionManager.showAccessoryPicker()
                        }) {
                            Text("重新建立连接")
                                .foregroundColor(.blue)
                        }
                        .buttonStyle(.plain)
                        .padding(.leading, 48)
                        
                        InstructionsRow(
                            icon: "arrow.down.circle",
                            title: "主板固件",
                            description: "OTA 更新需要将主板连接到本地 WLAN。或者可以使用 LTS 设计网站上的网页烧录器。"
                        )
                        .padding(.top, 26)
                        
                        InstructionsRow(
                            icon: "exclamationmark.triangle",
                            title: "电机强度",
                            description: "如果电机发热或振动，请调整电机强度。电源适配器功率不足也会影响强度。"
                        )
                        .padding(.top, 26)
                        
                        InstructionsRow(
                            icon: "stop.circle",
                            title: "Auto-Stopp",
                            description: "灵敏度取决于电源适配器。如果电机频繁停止，请在设置中降低灵敏度。"
                        )
                        .padding(.top, 26)
                        
                        InstructionsRow(
                            icon: "chevron.left.forwardslash.chevron.right",
                            title: "GitHub",
                            description: "源代码及所有其他文件均为开源，可在 [GitHub](https://github.com/LukasT03/LTS-Respooler) 下载。"
                        )
                        .padding(.top, 26)
                        
                        InstructionsRow(
                            icon: "exclamationmark.bubble",
                            title: "Feedback",
                            description: "如有问题、困难或建议，欢迎发送邮件至 info@lts-design.com。"
                        )
                        .padding(.top, 26)
                    }
                    .padding(.top, 12)
                    .padding(.horizontal, 20)
                    .padding(.trailing, 20)
                    .frame(maxWidth: .infinity, alignment: .topLeading)
                    .padding(.bottom, layoutModel.isCompactWidth ? 0 : 16)
                }
            }
            .frame(maxHeight: .infinity, alignment: .top)
            .navigationTitle("说明")
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button {
                        dismiss()
                    } label: {
                        if #available(iOS 26, *) {
                            Image(systemName: "xmark")
                        } else {
                            Text("关闭")
                        }
                    }
                }
            }
        }
    }
}

struct InstructionsRow: View {
    let icon: String
    let title: LocalizedStringKey
    let description: LocalizedStringKey

    var body: some View {
        HStack(alignment: .top, spacing: 20) {
            Image(systemName: icon)
                .resizable()
                .scaledToFit()
                .frame(width: 28)
                .padding(.top, 4)
            VStack(alignment: .leading) {
                Text(title)
                    .font(.headline)
                    .bold()
                Text(description)
                    .foregroundColor(.secondary)
            }
            .fixedSize(horizontal: false, vertical: true)
        }
    }
}

#if DEBUG
#Preview("Instructions") {
    InstructionsView()
        .environment(AccessorySessionManager())
}
#endif
