import SwiftUI

struct SplashView: View {
    @Environment(AccessorySessionManager.self) private var accessorySessionManager

    var body: some View {
        GeometryReader { geometry in
            ZStack(alignment: .topTrailing) {
                VStack {
                    
                    Spacer(minLength: 60)
                
                Image("AppIconSquare")
                    .resizable()
                    .scaledToFit()
                    .frame(width: 130)
                    .shadow(color: Color.black.opacity(0.1), radius: 12)
                
                Spacer()
                
                HStack {
                    Text("欢迎使用 LTS Control")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 40)
                }
                .frame(maxWidth: 500)
            
                Spacer()
                
                VStack(alignment: .leading, spacing: 27) {
                    FeatureRow(
                        icon: "gearshape",
                        title: "功能",
                        description: "Um das Respooler Board mit der App zu steuern, musst du es zuerst mit deinem \(UIDevice.current.userInterfaceIdiom == .pad ? "iPad" : "iPhone") verbinden."
                    )
                    FeatureRow(
                        icon: "antenna.radiowaves.left.and.right",
                        title: "连接",
                        description: "请确保主板已开启，然后点击下方按钮开始配对。"
                    )
                }
                .padding(.leading, 30)
                .padding(.trailing, 42)
                
                Spacer()
        
                Button(action: {
                    accessorySessionManager.showAccessoryPicker()
                }) {
                    Text("连接倒料器")
                        .fontWeight(.semibold)
                        .frame(minWidth: 0, maxWidth: 360)
                }
                .focusable(false)
                .padding(.vertical, 15)
                .background(Color.blue)
                .foregroundColor(.white)
                .clipShape(RoundedRectangle(cornerRadius: 16, style: .continuous))
                .padding(.horizontal, 26)
                .padding(.bottom, 38)
                }
            }
        }
        .frame(minWidth: 0, maxWidth: {
            return UIDevice.current.userInterfaceIdiom == .pad ? 480 : 393
        }(), minHeight: 23)
    }
}

#Preview {
    SplashView()
        .environment(AccessorySessionManager())
}

struct FeatureRow: View {
    let icon: String
    let title: LocalizedStringKey
    let description: LocalizedStringKey

    var body: some View {
        HStack(alignment: .center, spacing: 18) {
            Image(systemName: icon)
                .resizable()
                .scaledToFit()
                .frame(width: 36, height: 36)
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
