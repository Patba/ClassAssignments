Sub Zadanie1()
    Dim rng         As Range
    Dim Cell
    Dim lowerbound  As Integer
    Dim upperbound  As Integer
    Dim highestValue
    Dim Response
    
    Dim choice
    
    choice = 6
    
    Do While choice = 6
        
        'Definiowanie range komorek'
        
        Set rng = Application.InputBox("Wybierz komorki", "Range", Type:=8)
        MsgBox "The Range Is " & rng.Address
        
        'Ustalenie granic'
        
        lowerbound = InputBox("Gorna wartosc", "Losowanie")
        upperbound = InputBox("Dolna wartosc", "Losowanie")
        
        'Dla kazdej komorki losujemy z przedzialu'
        
        For Each Cell In rng
            Cell.Value = Int(lowerbound + Rnd * (upperbound - lowerbound + 1))
        Next Cell
        
        'Szukanie modulo'
        
        highestValue = 0
        
        For Each Cell In rng
            If Cell.Value Mod 3 = 0 Then
                If Cell.Value > highestValue Then highestValue = Cell.Value
            End If
        Next
        
        'MsgBox typu Czy Kontunuujemy?'
        
        Response = MsgBox("Najwieksze modulo: " & highestValue & " Czy przeszukujemy kolejny obszar?", vbYes & vbNo, "Decyzja?")
        
        If Response = 7 Then
            
            Exit Do
            
        End If
        
    Loop
    
End Sub