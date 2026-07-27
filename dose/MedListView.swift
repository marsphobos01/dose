//
//  MedListView.swift
//  Dose
//
//  Created by Morgan Bennett on 26/07/2026.
//

import SwiftUI
import SwiftData

struct MedListView: View {
    @Query var meds: [Med]
    var body: some View {
        List(meds) { med in Text(med.name)}
    }
}

#Preview {
    MedListView()
}
