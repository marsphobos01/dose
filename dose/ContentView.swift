import SwiftUI
import Playgrounds
import SwiftData

@main struct DoseApp: App {
    var body: some Scene {
        WindowGroup {
            MedListView()
                .modelContainer(for: Med.self)
        }
    }
}

struct ContentView: View {
    var body: some View {
        Text("Hello, world!")
            .padding()
    }
}

#Preview {
    ContentView()
}

#Playground {
    _ = 1 + 2
}
